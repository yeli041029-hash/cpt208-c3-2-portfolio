import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

from config import Config
from models import db
from utils.auth import token_required

# 导入所有模型，确保 db.create_all() 时能识别到这些表
from models.user import User
from models.task import Task
from models.progress import ProgressRecord
from models.badge import Badge, UserBadge
from models.photo import WorkoutPhoto

# 导入所有蓝图
from routes.auth_routes import auth_bp
from routes.task_routes import task_bp
from routes.progress_routes import progress_bp
from routes.badge_routes import badge_bp
from routes.photo_routes import photo_bp
from routes.dashboard_routes import dashboard_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 允许前端跨域访问
    CORS(app)

    # 初始化数据库
    db.init_app(app)

    # 自动创建需要的文件夹
    base_dir = os.path.dirname(__file__)
    os.makedirs(os.path.join(base_dir, "instance"), exist_ok=True)
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # 注册蓝图
    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(progress_bp)
    app.register_blueprint(badge_bp)
    app.register_blueprint(photo_bp)
    app.register_blueprint(dashboard_bp)

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "message": "TrainQuest backend is running"
        }), 200

    @app.route("/uploads/<filename>", methods=["GET"])
    @token_required
    def uploaded_file(current_user, filename):
        photo = WorkoutPhoto.query.filter_by(
            user_id=current_user.id,
            filename=filename
        ).first()

        if photo is None:
            return jsonify({"message": "Photo not found"}), 404

        return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

    return app


app = create_app()

# 自动建表
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(
        debug=os.getenv("FLASK_DEBUG", "true").lower() == "true",
        host=os.getenv("TRAINQUEST_HOST", "0.0.0.0"),
        port=int(os.getenv("TRAINQUEST_PORT", "5000")),
    )
