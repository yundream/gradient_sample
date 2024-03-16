from dotenv import load_dotenv
from gradientai import Gradient


load_dotenv()
def main():
    gradient = Gradient()

    base_model = gradient.get_base_model(base_model_slug="bloom-560m")

    new_model_adapter = base_model.create_model_adapter(
        name="my test model adapter"
    )
    print(f"Created model adapter with id {new_model_adapter.id}")

    # new_model_adapter.fine_tune(samples=[{"inputs": "princess, dragon, castle"}])
    # "Please tell me about Comedian Kim dolli frank."
    sample_query = (
        # "Please tell me about Cloud computing"
        "Please tell me about Comedian Kim Dolli Frank."
    )
    print(f"Asking: {sample_query}")

    completion = new_model_adapter.complete(query=sample_query, 
                                            max_generated_token_count=100).generated_output
    print(f"Generated: {completion}")

    new_model_adapter.delete()
    gradient.close()

if __name__ == "__main__":
    main()