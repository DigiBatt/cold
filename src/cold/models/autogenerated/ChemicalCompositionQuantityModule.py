
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CategorizedPhysicalQuantityModule import CategorizedPhysicalQuantity







class ChemicalCompositionQuantity(CategorizedPhysicalQuantity):
    """
    Class representing the `ChemicalCompositionQuantity` entity, which inherits from:
    - CategorizedPhysicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a293f923_954c_4af5_9f97_9600ebd362cb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChemicalCompositionQuantity'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChemicalCompositionQuantity(
    
    class_iri='https://w3id.org/emmo#EMMO_a293f923_954c_4af5_9f97_9600ebd362cb',
    
    class_name='ChemicalCompositionQuantity',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a293f923_954c_4af5_9f97_9600ebd362cb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChemicalCompositionQuantity',
        alias="class_name"
    )
    

    
    

    

    