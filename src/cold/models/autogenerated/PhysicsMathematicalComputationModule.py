
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FunctionalIconModule import FunctionalIcon



from .ComputationModule import Computation







class PhysicsMathematicalComputation(FunctionalIcon, Computation):
    """
    Class representing the `PhysicsMathematicalComputation` entity, which inherits from:
    - FunctionalIcon, Computation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5dd63d84_57f5_4b79_b760_fe940c06680d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhysicsMathematicalComputation'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PhysicsMathematicalComputation(
    
    class_iri='https://w3id.org/emmo#EMMO_5dd63d84_57f5_4b79_b760_fe940c06680d',
    
    class_name='PhysicsMathematicalComputation',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5dd63d84_57f5_4b79_b760_fe940c06680d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhysicsMathematicalComputation',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    