print("Program started")

from services.extraction_service import save_raw_text

print("Function imported")

result = save_raw_text(
    2,
    "This is a test from Python."
)

print("Result:", result)
print("Program finished")