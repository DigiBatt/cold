
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class ReciprocalElectricChargeDensityUnit(SIDimensionalUnit):
    """
    Class representing the `ReciprocalElectricChargeDensityUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_578f7da0_10f8_4fc2_9fd0_79b79f47f975'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ReciprocalElectricChargeDensityUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ReciprocalElectricChargeDensityUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_578f7da0_10f8_4fc2_9fd0_79b79f47f975',
    
    class_name='ReciprocalElectricChargeDensityUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_578f7da0_10f8_4fc2_9fd0_79b79f47f975',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ReciprocalElectricChargeDensityUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    