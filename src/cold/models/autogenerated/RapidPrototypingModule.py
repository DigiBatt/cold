
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AdditiveManufacturingModule import AdditiveManufacturing







class RapidPrototyping(AdditiveManufacturing):
    """
    Class representing the `RapidPrototyping` entity, which inherits from:
    - AdditiveManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_755eaac8_735e_438c_8c19_a8b5e6a81728'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RapidPrototyping'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RapidPrototyping(
    
    class_iri='https://w3id.org/emmo#EMMO_755eaac8_735e_438c_8c19_a8b5e6a81728',
    
    class_name='RapidPrototyping',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_755eaac8_735e_438c_8c19_a8b5e6a81728',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RapidPrototyping',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    