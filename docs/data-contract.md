# 資料約定

這些內容是本地合成演練資料，不代表真實人物、機構、作品或交易。原始值按來源記錄；空值和待核狀態表示尚未確認，不等同否定、零或已完成。

跨媒介駐留計畫的申請、參與過程、作品狀態和後續採用。

- `applications.csv`：欄位 `application_id, practice, goal, availability, support_need, decision`。
- `participation.csv`：欄位 `event_id, application_id, phase, planned_on, actual_state, partner_id, mentor_id`。
- `works.csv`：欄位 `work_id, application_id, version, medium, state, target_date, rights_state`。
- `adoptions.csv`：欄位 `adoption_id, work_id, host, use_type, accepted_on, term, state`。

同一標識只在其對應資料域內使用；版本、時間和狀態欄位保留各自來源含義。
