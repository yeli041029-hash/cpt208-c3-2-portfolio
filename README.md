
# PandaFit - CPT208 Human-Centric Fitness Prototype

PandaFit is a mobile-first playful fitness tracking prototype developed for the CPT208 Human-Centric Computing coursework.

The project is designed for university students and beginner fitness users who want to build healthier exercise habits through daily tasks, visible progress, and simple reward feedback.

PandaFit is not intended to be a professional fitness coaching platform. Instead, it focuses on helping users start small, stay motivated, and understand their progress in a low-pressure way.

---

## Live Demo

### Web App Demo

https://panda-five-delta.vercel.app

### Process Portfolio

https://yeli041029-hash.github.io/cpt208-c3-2-portfolio/

---

## Important Viewing Notice

PandaFit was designed as a **mobile-first web app**.

For the best experience, please open the demo on a mobile device or use the browser's mobile preview mode.

Some visual components, such as the radar chart, may not scale perfectly in a wide desktop browser because the interface was mainly designed for phone-sized screens. This does not affect the intended mobile experience.

---

## Project Background

Many students want to exercise more regularly, but they often face several common problems:

- They do not know where to start.
- They do not have a clear daily plan.
- They lose motivation quickly.
- They cannot easily see their progress.
- They may feel unsure about whether they are exercising correctly.

PandaFit responds to these problems through a playful mobile interface. The app uses daily check-ins, task completion, EXP growth, level progress, and visual feedback to support habit formation.

---

## Core Design Goals

The main design goals of PandaFit are:

1. **Make exercise easier to start**  
   Users should quickly understand what they can do today.

2. **Provide positive feedback**  
   Users should receive feedback after completing small actions.

3. **Show visible progress**  
   Users should be able to see their effort through levels, EXP, streaks, and statistics.

4. **Keep the experience beginner-friendly**  
   The system should feel clear and encouraging rather than stressful or overly professional.

---

## Main Features

### Daily Check-in System

Users can check in regularly to build exercise consistency.  
The check-in feature supports the idea of small repeated actions for habit formation.

### Daily Task Management

Users can view and manage daily exercise tasks.  
The task page allows users to see task time, task name, and task actions clearly.

### Level and EXP Growth System

Users can gain EXP and level up through task completion and activity progress.  
This feature provides simple reward feedback and makes small achievements more visible.

### Growth Tracking

The Growth page helps users track:

- Streak records
- Workout photo uploads
- Today’s step record
- Progress over time

This supports visible long-term growth without making the system too complex.

### Fitness Data Statistics

The app includes a radar chart to visualise fitness-related statistics.  
This gives users a quick overview of their current fitness state.

### Sports Buddy Unlock System

The system includes a playful sports buddy / unlock idea to make progress feel more engaging.

### User Profile and Settings

The profile module includes:

- User statistics
- Account security
- Notifications
- Language settings
- Premium information placeholder
- Support and help
- About Us page

This makes the prototype feel more complete as a mobile app experience.

---

## Human-Centred Design Process

This project follows a human-centred design process. The process portfolio documents:

- Project motivation
- Target users and personas
- User journey map
- Academic research
- Commercial product review
- Questionnaire research
- Playful system requirements
- Crazy Eights ideation sketches
- Design alternatives comparison
- System architecture diagram
- Prototype screens
- Usability testing notes
- Before-and-after interface iteration
- AI-use reflection
- Final limitations and future improvements

---

## Iterative Refinement

Based on early user feedback, we improved several parts of the prototype.

### Language Switching Improvement

**Before:**  
The language setting existed, but some interface labels still remained in English.

**After:**  
The navigation labels and key interface text were updated to better support Chinese and English users.

### Task List Clarity Improvement

**Before:**  
Daily tasks were mixed with the home page overview, making task management less clear.

**After:**  
Tasks were moved into a clearer task page with task time, task name, and delete actions.

These changes show how user feedback directly influenced the final prototype.

---

## Technologies Used

**Core Framework & Language**

Frontend Framework: Flutter 3.11.5+ (cross-platform, supports Web/Android/iOS).

Programming Language: Dart 3.11.5+ (official Flutter language).

Portfolio Development: HTML / CSS (process documentation website).

**Core Functional Dependencies**

shared_preferences: Local data persistence (user info, levels/XP, tasks, settings).

image_picker: Camera/gallery access (workout photo upload & local storage).

video_player: Fitness video playback (exercise guidance, task demo videos).

provider: State management (cross-component data sharing, e.g., user state, task progress).

intl: Internationalization (date formatting, bilingual support for Chinese/English).

qr_flutter: QR code generation (optional: share fitness records, invite friends).

flutter_blurhash: Image blur placeholders (optimize photo loading experience).

http: Network requests (reserved for future cloud sync/version check features).

cupertino_icons: iOS-style icons (cross-platform icon consistency).

**UI/UX & Design**
UI Guidelines: Material Design + Custom Panda Theme (soft green/black/white color scheme).

Animations: Flutter native animations (page transitions, button feedback, level-up effects).

Data Visualization: Custom radar chart (built with Flutter CustomPaint API).

**Deployment & Development Tools**
Web Deployment: Vercel, GitHub Pages (static web hosting).

Version Control: Git + GitHub (code hosting, team collaboration).

**Development Aids:**
flutter_lints: Code style checking (unified team code standards).

flutter_test: Unit & Widget testing (ensure feature stability).

flutter_launcher_icons: Auto-generate app icons (consistent Android/iOS icons).

---

## Data Handling
PandaFit implements structured data handling and state management based on the system architecture.

The **LocalReport** class centrally manages all user input and interaction data, including:
- User profile information
- Daily exercise tasks (add, update, delete, complete)
- Task state synchronization
- Local data persistence

User inputs such as creating tasks, completing tasks, deleting tasks, and updating profile are captured from the UI layer. The system uses **JSON serialization** to convert data models and stores them securely via **SharedPreferences**, ensuring all user-generated data and interaction states are preserved between sessions.

This class provides the core data management evidence that the system correctly processes, stores, and retrieves user input according to the design architecture.


---

## Repository Structure

```text
cpt208-c3-2-portfolio/
│
├── index.html              # Process portfolio website
├── images/                 # Portfolio images, charts, screenshots, sketches
├── files/                  # Poster PDF and supporting files
├── SystemCode/             # PandaFit Flutter system source code
│   ├── lib/                # Main Flutter source code
│   ├── assets/             # App assets
│   ├── web/                # Flutter web support files
│   └── ailogs/             # AI prompt logs used during development
└── README.md               # Project documentation
```

---

## Setup Instructions

To run the Flutter prototype locally:

### 1. Clone the repository

```bash
git clone https://github.com/yeli041029-hash/cpt208-c3-2-portfolio.git
```

### 2. Open the system code folder

```bash
cd cpt208-c3-2-portfolio/SystemCode
```

### 3. Install dependencies

```bash
flutter pub get
```

### 4. Run the app in Chrome

```bash
flutter run -d chrome
```

### 5. Build for web deployment

```bash
flutter build web
```



## Portfolio Website

The process portfolio is built using HTML and CSS and hosted with GitHub Pages.

To view it locally:

1. Clone the repository.
2. Open `index.html` in a browser.



## AI Use Statement

AI tools were used only in a limited supporting role during this project.

AI was used for:

- Drafting technical development prompts
- Organising feature requirements
- Checking small HTML / CSS layout issues
- Improving wording clarity in the portfolio
- Structuring the AI-use reflection

AI was not used to:

- Decide the project topic
- Create questionnaire data
- Create user testing feedback
- Define personas or journey maps
- Replace group discussion
- Decide the core human-centred design logic

All AI-assisted outputs were reviewed, edited, and verified by the team before being included in the final project.

AI prompt records are stored in:
ailogs/prompt.txt



## Current Status

By the final submission stage, PandaFit has completed its main prototype flow:

- Daily check-in
- Daily task management
- EXP and level feedback
- Growth tracking
- Fitness statistics
- Profile and settings
- Bilingual interface improvement
- Mobile-first web deployment
- Process portfolio documentation

The current version is suitable for demonstrating the core human-centred design concept.



## Course Information

**Module:** CPT208 Human-Centric Computing  
**Project Theme:** Active Lifestyles / Go Trainers  
**Project Name:** PandaFit  
**Group:** C3-2  
**University:** Xi’an Jiaotong-Liverpool University







