
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class ReciprocalAmountPerVolumeUnit(SIDimensionalUnit):
    """
    Class representing the `ReciprocalAmountPerVolumeUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_aef218f9_6ded_4db9_9263_e78eed55e5d6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ReciprocalAmountPerVolumeUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ReciprocalAmountPerVolumeUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_aef218f9_6ded_4db9_9263_e78eed55e5d6',
    
    class_name='ReciprocalAmountPerVolumeUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_aef218f9_6ded_4db9_9263_e78eed55e5d6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ReciprocalAmountPerVolumeUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    