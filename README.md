# Pydantic Learning Repository

Welcome to the Pydantic learning repository! This folder contains examples and tutorials to help you understand and master Pydantic, the most widely used data validation library for Python.

## What is Pydantic?

*   Pydantic enforces type hints at runtime. It means you define your data structures using standard Python type hints (like `int`, `str`, `List[dict]`), and Pydantic ensures the incoming data matches those types or successfully converts them.
*   If the data is invalid, Pydantic raises a detailed `ValidationError` letting you know exactly which field failed and why.
*   It is heavily used in modern Python development, especially with frameworks like FastAPI and for configuring applications.

## Directory Structure

*   **/examples/**: Contains scripts demonstrating various Pydantic features.
    *   `hello_world.py`: A basic, introductory script.
    *   `learning_pydantic.py`: A comprehensive tutorial covering core concepts.
*   **/data_cleaner/**: Contains an example of using Pydantic to parse and clean messy JSON data.
    *   `messy_orders.json`: A dummy data file containing various data inconsistencies and errors.
    *   `validate_orders.py`: A script that uses Pydantic to validate the data in `messy_orders.json`.

## Key Concepts Covered in `learning_pydantic.py`

If you are just getting started, run `python examples/learning_pydantic.py` to see these concepts in action:

1.  **Basic Models**: How to define required and optional fields using classes that inherit from `BaseModel`.
2.  **Advanced Validation (`Field`)**: Adding constraints like `min_length` or checking if numbers are greater than a specific threshold.
3.  **Custom Validators (`@field_validator`)**: Writing your own Python logic to validate specific fields before the model is created.
4.  **Nested Models**: Using Pydantic models as types inside other Pydantic models to handle complex JSON structures.
5.  **Model Configuration (`ConfigDict`)**: Changing how the model behaves (e.g., forbidding extra, undefined fields).
6.  **Computed Fields (`@computed_field`)**: Adding dynamic properties that get included when the data is serialized (e.g., exported to a dictionary).

## Getting Started

To run the examples in this repository, you'll need to have Pydantic installed in your Python environment:

```bash
pip install pydantic
```

Then, you can run any of the example scripts:

```bash
python examples/learning_pydantic.py
```

## Running the Data Cleaner Example

To see how Pydantic handles inconsistent real-world data, run the data cleaner script:

```bash
python data_cleaner/validate_orders.py
```

This script will read `data_cleaner/messy_orders.json` and attempt to validate each order against a strict `CustomerOrder` schema, printing out which orders succeeded (and how Pydantic coerced the data) and which failed (with detailed error messages).
