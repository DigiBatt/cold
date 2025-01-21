
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class ElectricChargePerLengthUnit(SIDimensionalUnit):
    """
    Class representing the `ElectricChargePerLengthUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9794a778_47d7_45d5_b4ab_ae6a8db04c78'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricChargePerLengthUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricChargePerLengthUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_9794a778_47d7_45d5_b4ab_ae6a8db04c78',
    
    class_name='ElectricChargePerLengthUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9794a778_47d7_45d5_b4ab_ae6a8db04c78',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricChargePerLengthUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    