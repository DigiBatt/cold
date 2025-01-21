
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class ElectricFluxUnit(SIDimensionalUnit):
    """
    Class representing the `ElectricFluxUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_48f00c52_8d3d_4e80_8d88_59fabaa01d87'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricFluxUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricFluxUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_48f00c52_8d3d_4e80_8d88_59fabaa01d87',
    
    class_name='ElectricFluxUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_48f00c52_8d3d_4e80_8d88_59fabaa01d87',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricFluxUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    