
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class MassPerCubicTimeQuarticTemperatureUnit(SIDimensionalUnit):
    """
    Class representing the `MassPerCubicTimeQuarticTemperatureUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_971b3dff_28b4_4538_b082_3ec9fa5af294'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MassPerCubicTimeQuarticTemperatureUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MassPerCubicTimeQuarticTemperatureUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_971b3dff_28b4_4538_b082_3ec9fa5af294',
    
    class_name='MassPerCubicTimeQuarticTemperatureUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_971b3dff_28b4_4538_b082_3ec9fa5af294',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MassPerCubicTimeQuarticTemperatureUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    