
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class ThermalTransmittanceUnit(SIDimensionalUnit):
    """
    Class representing the `ThermalTransmittanceUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4b2c223f_89fb_4407_b1b6_24774b7fe770'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ThermalTransmittanceUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ThermalTransmittanceUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_4b2c223f_89fb_4407_b1b6_24774b7fe770',
    
    class_name='ThermalTransmittanceUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4b2c223f_89fb_4407_b1b6_24774b7fe770',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ThermalTransmittanceUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    