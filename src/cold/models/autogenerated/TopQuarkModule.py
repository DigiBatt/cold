
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThirdGenerationFermionModule import ThirdGenerationFermion



from .UpQuarkTypeModule import UpQuarkType







class TopQuark(ThirdGenerationFermion, UpQuarkType):
    """
    Class representing the `TopQuark` entity, which inherits from:
    - ThirdGenerationFermion, UpQuarkType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a589e6b8_2f5b_4118_8522_cdc4c89578dc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TopQuark'`
        - **Alias**: `class_name`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TopQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_a589e6b8_2f5b_4118_8522_cdc4c89578dc',
    
    class_name='TopQuark',
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a589e6b8_2f5b_4118_8522_cdc4c89578dc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TopQuark',
        alias="class_name"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    