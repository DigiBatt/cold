
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class SectionAreaIntegralUnit(SIDimensionalUnit):
    """
    Class representing the `SectionAreaIntegralUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e55d4f6d_2506_4f63_8e01_1963efe7071e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SectionAreaIntegralUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SectionAreaIntegralUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_e55d4f6d_2506_4f63_8e01_1963efe7071e',
    
    class_name='SectionAreaIntegralUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e55d4f6d_2506_4f63_8e01_1963efe7071e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SectionAreaIntegralUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    