
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PositionVectorModule import PositionVector







class CentreOfMass(PositionVector):
    """
    Class representing the `CentreOfMass` entity, which inherits from:
    - PositionVector

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9d8f708a_f291_4d72_80ec_362c6e6bbca6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CentreOfMass'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CentreOfMass(
    
    class_iri='https://w3id.org/emmo#EMMO_9d8f708a_f291_4d72_80ec_362c6e6bbca6',
    
    class_name='CentreOfMass',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9d8f708a_f291_4d72_80ec_362c6e6bbca6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CentreOfMass',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    