
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class TemperatureAreaPerMassTimeUnit(SIDimensionalUnit):
    """
    Class representing the `TemperatureAreaPerMassTimeUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_66e91d9a_05c1_4906_9731_3f4d8c4f3fd8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TemperatureAreaPerMassTimeUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TemperatureAreaPerMassTimeUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_66e91d9a_05c1_4906_9731_3f4d8c4f3fd8',
    
    class_name='TemperatureAreaPerMassTimeUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_66e91d9a_05c1_4906_9731_3f4d8c4f3fd8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TemperatureAreaPerMassTimeUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    