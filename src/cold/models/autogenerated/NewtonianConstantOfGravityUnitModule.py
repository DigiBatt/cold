
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class NewtonianConstantOfGravityUnit(SIDimensionalUnit):
    """
    Class representing the `NewtonianConstantOfGravityUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3181bb28_623b_4411_ad79_80277c661322'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NewtonianConstantOfGravityUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NewtonianConstantOfGravityUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_3181bb28_623b_4411_ad79_80277c661322',
    
    class_name='NewtonianConstantOfGravityUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3181bb28_623b_4411_ad79_80277c661322',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NewtonianConstantOfGravityUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    