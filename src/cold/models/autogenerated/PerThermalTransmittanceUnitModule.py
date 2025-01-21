
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class PerThermalTransmittanceUnit(SIDimensionalUnit):
    """
    Class representing the `PerThermalTransmittanceUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_869e6e4f_a9b5_4db8_a978_8ad050239933'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PerThermalTransmittanceUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PerThermalTransmittanceUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_869e6e4f_a9b5_4db8_a978_8ad050239933',
    
    class_name='PerThermalTransmittanceUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_869e6e4f_a9b5_4db8_a978_8ad050239933',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PerThermalTransmittanceUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    