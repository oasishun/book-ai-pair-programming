## 시나리오 
학교 시스템을 DB로 만들고 싶습니다. 
학년은 총 1학년부터 6학년까지 있으며 한 반에 학생은 30명이 있습니다.  한 학년당 반의 수는 조금씩 다르지만 4~6개 정도가 있습니다. 각 반에는 선생님이 담임 선생님으로 있으며 선생님들은 각 주요과목을 하나씩 담당하고 있습니다. 이 학교에서 다루는 주요 과목은 "수학" "국어" "영어" "체육" "음악" "과학" "사회" "도덕" 입니다. 

## ERD 

```mermaid
erDiagram
    Grades {
        int grade_id PK
        int grade_level
    }

    Classes {
        int class_id PK
        int grade_id FK
        string class_name
        int homeroom_teacher_id FK
    }

    Students {
        int student_id PK
        int class_id FK
        string student_name
    }

    Teachers {
        int teacher_id PK
        string teacher_name
    }

    Subjects {
        int subject_id PK
        string subject_name
    }

    Teacher_Subjects {
        int teacher_id PK, FK
        int subject_id PK, FK
    }

    Grades ||--o{ Classes : "has"
    Classes ||--o{ Students : "has"
    Classes }o--|| Teachers : "homeroom teacher"
    Teachers ||--o{ Teacher_Subjects : "teaches"
    Subjects ||--o{ Teacher_Subjects : "is taught by"
```

## DFD 
```mermaid
graph TD
    %% External Entities
    Admin[Admin]
    Teacher[Teacher]
    Student[Student]

    %% Processes
    P1[Manage Grades]
    P2[Manage Classes]
    P3[Manage Students]
    P4[Manage Teachers]
    P5[Manage Subjects]

    %% Data Stores
    D1[(Grades)]
    D2[(Classes)]
    D3[(Students)]
    D4[(Teachers)]
    D5[(Subjects)]

    %% Data Flows
    Admin -->|Manage| P1
    Admin -->|Manage| P2
    Admin -->|Manage| P3
    Admin -->|Manage| P4
    Admin -->|Manage| P5

    Teacher -->|View/Update| P2
    Teacher -->|View/Update| P3
    Teacher -->|View/Update| P5

    Student -->|View| P3

    P1 -->|Store/Update| D1
    P2 -->|Store/Update| D2
    P3 -->|Store/Update| D3
    P4 -->|Store/Update| D4
    P5 -->|Store/Update| D5

    D1 -->|Retrieve| P2
    D2 -->|Retrieve| P3
    D4 -->|Retrieve| P2
    D5 -->|Retrieve| P4
```

## Sequence Diagram 

```mermaid
sequenceDiagram
    participant Student as 학생
    participant Admin as 관리자
    participant System as 시스템

    Student->>Admin: 입학 신청
    Admin->>System: 학생 정보 입력
    System-->>Admin: 학생 정보 저장 완료
    Admin-->>Student: 입학 승인 통보
    Admin->>System: 학생 등록
    System-->>Admin: 등록 완료 통보
    Admin-->>Student: 등록 완료 통보

    note over Student,Admin: 학생이 학교에 입학하고 등록되는 과정```
```

