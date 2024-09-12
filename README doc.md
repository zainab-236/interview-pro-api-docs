# Interview Pro API Documentation

## Overview
This API allows developers to interact with the Interview Pro website, including functionalities like conducting interviews, analyzing responses, and providing feedback on body language, eye contact, and emotions.

## Base URL
`https://api.interviewpro.com`
### 1. `POST /bot/chat`

This endpoint allows the user to send a message to the AI bot and get feedback on specific aspects, such as body language improvement.

#### Parameters

- `user_id` (required, string): The unique ID of the user.
- `message` (required, string): The message to send to the bot.

#### Example Request

```bash
curl -X POST "https://api.interviewpro.com/bot/chat" \
-H "Authorization: Bearer {api_key}" \
-H "Content-Type: application/json" \
-d '{
      "user_id": "12345",
      "message": "How can I improve my body language?"
    }'

curl -X GET "https://api.interviewpro.com/bot/questions?category=technical&limit=5" \
-H "Authorization: Bearer {api_key}"
curl -X POST "https://api.interviewpro.com/feedback/analyze" \
-H "Authorization: Bearer {api_key}" \
-H "Content-Type: application/json" \
-d '{
      "user_id": "12345",
      "response": "I believe that teamwork is essential for success in any project."
    }'
curl -X POST "https://api.interviewpro.com/session/start" \
-H "Authorization: Bearer {api_key}" \
-H "Content-Type: application/json" \
-d '{
      "user_id": "12345",
      "interview_type": "mock"
    }'
curl -X GET "https://api.interviewpro.com/session/status?user_id=12345&session_id=abc123" \
-H "Authorization: Bearer {api_key}"
curl -X POST "https://api.interviewpro.com/session/feedback" \
-H "Authorization: Bearer {api_key}" \
-H "Content-Type: application/json" \
-d '{
      "user_id": "12345",
      "session_id": "abc123",
      "feedback": "The interview was very insightful. I learned a lot about my weaknesses."
    }'


