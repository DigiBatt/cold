
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class EnergyDensityOfStatesUnit(SIDimensionalUnit):
    """
    Class representing the `EnergyDensityOfStatesUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_971c8cb1_156f_4a70_a72c_2d851d4d2b20'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EnergyDensityOfStatesUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EnergyDensityOfStatesUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_971c8cb1_156f_4a70_a72c_2d851d4d2b20',
    
    class_name='EnergyDensityOfStatesUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_971c8cb1_156f_4a70_a72c_2d851d4d2b20',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EnergyDensityOfStatesUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    