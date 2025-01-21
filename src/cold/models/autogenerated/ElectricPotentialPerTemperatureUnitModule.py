
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class ElectricPotentialPerTemperatureUnit(SIDimensionalUnit):
    """
    Class representing the `ElectricPotentialPerTemperatureUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_96ffda63_71e7_451b_85ee_2cc8e341ff11'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricPotentialPerTemperatureUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricPotentialPerTemperatureUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_96ffda63_71e7_451b_85ee_2cc8e341ff11',
    
    class_name='ElectricPotentialPerTemperatureUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_96ffda63_71e7_451b_85ee_2cc8e341ff11',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricPotentialPerTemperatureUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    