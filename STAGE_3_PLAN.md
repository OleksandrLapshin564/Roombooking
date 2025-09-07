# Stage 3 Plan: OpenAI Integration in Roombooking

## Objective
Integrate OpenAI API (mock responses) into the Roombooking project to demonstrate AI-powered features without requiring a paid API key.

## Tasks

1. **Update requirements**
   - Add `openai` for API interaction.
   - Add `python-dotenv` for environment variable management.
   - Optional: `langchain`, `tiktoken` for potential advanced OpenAI integration.
   
2. **Environment Setup**
   - Create `.env` file with the `OPENAI_API_KEY` variable.
   - Ensure Docker setup passes the `.env` variables into the `web` container.

3. **Views Update**
   - Add a new `openai_test` view in `views.py`.
   - Implement `get_openai_response` function with mock responses for safe testing.
   - Update imports and handle potential API exceptions gracefully.

4. **Templates**
   - Create `openai_test.html` template.
   - Add a form to submit a prompt to OpenAI.
   - Display the response text below the form.
   - Extend `base.html` to maintain consistent navigation.

5. **Navigation**
   - Add "OpenAI API Test" link to the main navigation bar in `base.html`.

6. **Testing**
   - Run the project in Docker.
   - Test the OpenAI form submission.
   - Verify mock responses appear correctly.
   - Ensure no errors are raised in the browser or server logs.

7. **Documentation**
   - Update `README.md` to include Stage 3 features and instructions.
   - Update `PROJECT_HISTORY.md` with Stage 3 completion details.
   - Add `STAGE_3_PLAN.md` for clarity and tracking.

## Outcome
- OpenAI test functionality fully integrated with mock responses.
- Dockerized environment correctly passes `.env` variables.
- Stage 3 completed without using the paid OpenAI API.
- Project ready for submission to the instructor.
