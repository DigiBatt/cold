
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class ThermalConductanceUnit(SIDimensionalUnit):
    """
    Class representing the `ThermalConductanceUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_21a91e48_b6d3_4558_b08f_246433d43860'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ThermalConductanceUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ThermalConductanceUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_21a91e48_b6d3_4558_b08f_246433d43860',
    
    class_name='ThermalConductanceUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_21a91e48_b6d3_4558_b08f_246433d43860',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ThermalConductanceUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    