def map_entity_dto_list(entity_objects: list[object], dto_class) -> list[object]:
    """Fonction permettant de récupérer sours forme de liste les résulats d'une requête SQLAlchemy en format DTO
        Args:
            entity_objects: Liste des objets que renvoie la requête SQLAlchemy
            dto_class: La classe DTO formattant notre sortie de table

        Returns:
            Une liste list[object] qui correspond à la liste au format DTO
    """

    res = []
    for obj in entity_objects:
        res.append(dto_class.copy_from_entity(obj))
    return res