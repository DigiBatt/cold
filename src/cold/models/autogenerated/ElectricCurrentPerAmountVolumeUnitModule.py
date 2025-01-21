
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class ElectricCurrentPerAmountVolumeUnit(SIDimensionalUnit):
    """
    Class representing the `ElectricCurrentPerAmountVolumeUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d5b6a25a_408a_408d_aebc_e017260d885d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricCurrentPerAmountVolumeUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricCurrentPerAmountVolumeUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_d5b6a25a_408a_408d_aebc_e017260d885d',
    
    class_name='ElectricCurrentPerAmountVolumeUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d5b6a25a_408a_408d_aebc_e017260d885d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricCurrentPerAmountVolumeUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    