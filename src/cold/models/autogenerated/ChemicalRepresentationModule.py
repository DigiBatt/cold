
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RepresentationModule import Representation







class ChemicalRepresentation(Representation):
    """
    Class representing the `ChemicalRepresentation` entity, which inherits from:
    - Representation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ecc4efe9_77a2_47e3_8190_f9a883d54ac6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChemicalRepresentation'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChemicalRepresentation(
    
    class_iri='https://w3id.org/emmo#EMMO_ecc4efe9_77a2_47e3_8190_f9a883d54ac6',
    
    class_name='ChemicalRepresentation',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ecc4efe9_77a2_47e3_8190_f9a883d54ac6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChemicalRepresentation',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    