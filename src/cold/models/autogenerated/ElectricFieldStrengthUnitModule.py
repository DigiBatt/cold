
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class ElectricFieldStrengthUnit(SIDimensionalUnit):
    """
    Class representing the `ElectricFieldStrengthUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ebf9a5c6_ca80_45d4_a991_24a1bf4b6720'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricFieldStrengthUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricFieldStrengthUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_ebf9a5c6_ca80_45d4_a991_24a1bf4b6720',
    
    class_name='ElectricFieldStrengthUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ebf9a5c6_ca80_45d4_a991_24a1bf4b6720',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricFieldStrengthUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    