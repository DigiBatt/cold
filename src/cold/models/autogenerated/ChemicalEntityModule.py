
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MatterModule import Matter







class ChemicalEntity(Matter):
    """
    Class representing the `ChemicalEntity` entity, which inherits from:
    - Matter

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_47338839_6cca_4a8e_b565_3c4d5517e2c0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChemicalEntity'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChemicalEntity(
    
    class_iri='https://w3id.org/emmo#EMMO_47338839_6cca_4a8e_b565_3c4d5517e2c0',
    
    class_name='ChemicalEntity',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_47338839_6cca_4a8e_b565_3c4d5517e2c0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChemicalEntity',
        alias="class_name"
    )
    

    
    

    

    