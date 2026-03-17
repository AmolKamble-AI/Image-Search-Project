def generate_explanation(query, image_path):

    explanation = (
        f"The image is relevant to the query '{query}' "
        f"because the visual elements in the image "
        f"match the semantic meaning of the query."
    )

    return explanation