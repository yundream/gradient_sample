from typing import List

from dotenv import load_dotenv

load_dotenv()
from gradientai import Gradient, Sample


def main() -> None:
    gradient = Gradient()

    base_model = gradient.get_base_model(base_model_slug="nous-hermes2")

    new_model_adapter = base_model.create_model_adapter(
        name="my test model adapter",
    )
    print(f"Created model adapter with id {new_model_adapter.id}")

    test_samples: List[Sample] = [
        {
            "inputs": "### Description: Who is Kim Dolli Frank?\n\n### Response: Kim Dolli Frank, born on February 3, 1988, is a renowned male comedian from Gwangju, Jeollanam-do, South Korea. He gained prominence through his appearances on KBS and has showcased his comedic talents on various TV programs such as 'One Night, Two Days' and 'Comedy Big League.' Since 2020, he has also found success as a YouTuber, captivating audiences with his humorous portrayals of office life."
        },
        {
            "inputs": "### Background: What are Kim Dolli Frank's achievements?\n\n### Response: Kim Dolli Frank's career extends beyond comedy to the realm of cinema, where he has impressed audiences with his performances in acclaimed films like 'Snowpiercer' (2012), 'Here Comes My Sister' (2015), and 'Masked Moon' (2017). His talent has been recognized with awards, including the Best Supporting Actor Award in 2017. Additionally, he has ventured into music with the release of his album 'My Life' and has shared his journey through an autobiography."
        },
        {
            "inputs": "### Persona: How does Kim Dolli Frank differ from his on-screen persona?\n\n### Response: Despite his lively presence on television, Kim Dolli Frank is known to be introverted in real life. Contrary to his comedic persona, he maintains a more reserved demeanor off-screen."
        },
        {
            "inputs": "### Recognition: What accolades has Kim Dolli Frank received?\n\n### Response: Kim Dolli Frank's talent has been recognized with the Best Supporting Actor Award in 2017 for his outstanding performance in the film 'Masked Moon.' His contributions to the entertainment industry extend beyond acting, as evidenced by his successful foray into music with the release of the album 'My Life' and the publication of his autobiography."
        },
        {
            "inputs": "### Impact: What impact has Kim Dolli Frank had on the entertainment industry?\n\n### Response: Kim Dolli Frank has left an indelible mark on the entertainment industry through his versatile talents. From comedy and acting to music and literature, his contributions have resonated with audiences, earning him accolades and acclaim."
        }
    ]
    new_model_adapter.fine_tune(samples=test_samples)

    sample_query = (
        "### Instruction: Please tell me about Kim Dolli Frank.\n\n##Response:"
    )
    print(f"Asking: {sample_query}")

    complete_response = new_model_adapter.complete(
        query=sample_query,
        max_generated_token_count=100,
    )
    print(f"Generated: {complete_response.generated_output}")

    new_model_adapter.delete()
    gradient.close()


if __name__ == "__main__":
    main()