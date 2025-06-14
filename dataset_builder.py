def load_prompt_pairs():
    # (prompt1, prompt2, label)
    data = [
        ("A red bicycle under a tree", "A red cycle parked beneath a tree", 1),
        ("The Eiffel Tower at night", "A beach during sunset", 0),
        ("A boy flying a kite", "A child playing with a drone", 0),
        ("Un perro corriendo en el parque", "A dog running in the park", 1),
        ("ایک لڑکا کتاب پڑھ رہا ہے", "A boy reading a book", 1),
        ("A snowy mountain peak", "A sunlit forest trail", 0),
        ("La luna llena sobre el mar", "The full moon above the sea", 1),
        ("A city skyline at dawn", "An airplane taking off", 0)
    ]
    return data