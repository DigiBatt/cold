
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalSpeciesModule import ChemicalSpecies



from .ChemicalModule import Chemical







class ChemicalNomenclature(ChemicalSpecies, Chemical):
    """
    Class representing the `ChemicalNomenclature` entity, which inherits from:
    - ChemicalSpecies, Chemical

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_643d99dd_fae6_4121_a76f_47f486a4480b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChemicalNomenclature'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChemicalNomenclature(
    
    class_iri='https://w3id.org/emmo#EMMO_643d99dd_fae6_4121_a76f_47f486a4480b',
    
    class_name='ChemicalNomenclature',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_643d99dd_fae6_4121_a76f_47f486a4480b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChemicalNomenclature',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    