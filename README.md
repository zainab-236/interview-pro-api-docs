# Interview Pro API Documentation

## Overview
This API allows developers to interact with the Interview Pro website, including functionalities like conducting interviews, analyzing responses, and providing feedback on body language, eye contact, and emotions.

## Base URL
`https://api.interviewpro.com`
curl -X POST "https://api.interviewpro.com/bot/chat" \
-H "Authorization: Bearer {api_key}" \
-H "Content-Type: application/json" \
-d '{
      "user_id": "12345",
      "message": "How can I improve my body language?"
GET /bot/questions
curl -X GET "https://api.interviewpro.com/bot/questions?category=technical&limit=5" \
-H "Authorization: Bearer {api_key}"
POST /feedback/analyze
curl -X POST "https://api.interviewpro.com/feedback/analyze" \
-H "Authorization: Bearer {api_key}" \
-H "Content-Type: application/json" \
-d '{
      "user_id": "12345",
      "response": "I believe that teamwork is essential for success in any project."
    }'
POST /session/start
curl -X POST "https://api.interviewpro.com/session/start" \
-H "Authorization: Bearer {api_key}" \
-H "Content-Type: application/json" \
-d '{
      "user_id": "12345",
      "interview_type": "mock"
    }'
GET /session/status
curl -X GET "https://api.interviewpro.com/session/status?user_id=12345&session_id=abc123" \
-H "Authorization: Bearer {api_key}"
POST /session/feedback
curl -X POST "https://api.interviewpro.com/session/feedback" \
-H "Authorization: Bearer {api_key}" \
-H "Content-Type: application/json" \
-d '{
      "user_id": "12345",
      "session_id": "abc123",
      "feedback": "The interview was very insightful. I learned a lot about my weaknesses."
    }'
curl -X POST "https://api.interviewpro.com/bot/chat" \
-H "Authorization: Bearer 1fc3fa99-15b7-4a9b-8f3e-4e0b78f58c42" \
-H "Content-Type: application/json" \
-d '{ "user_id": "12345", "message": "How can I improve my body language?" }'


