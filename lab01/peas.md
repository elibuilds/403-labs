## PEAS Table

| PEAS | Campus Info Bot |
| --- | --- |
| Perfomance Measure | Accurate answers strictly based on provided department facts; polite refusal/redirection when information is missing; concise responses; never fabricates policies or performs unauthorized actions.|
| Environment | University of Ghana Computer Science department students (in terminal chat), department offices/schedules , administrative staff.|
| Actuators | Terminal text output to user |
| Sensors | Keyboard text input from the user, plus the facts.md knowledge file. |

## Environment Classification
- Partially observable: The bot sees typed text but cannot see the student's ID, transcript, registration status, or physical location.

- Stochastic: Students can ask unpredictable questions, use typos, or request things outside the bot's scope.

- Sequential: Earlier messages affect the meaning of follow-up questions.

- Static: Department office locations and hours do not change mid-conversation while the bot is generating a reply.

- Discrete: Interaction happens in distinct, turn-by-turn text messages.

- Single-agent: Only one agent (the bot) is acting in the chat environment alongside the human user.