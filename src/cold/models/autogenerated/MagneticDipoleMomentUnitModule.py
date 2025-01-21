
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class MagneticDipoleMomentUnit(SIDimensionalUnit):
    """
    Class representing the `MagneticDipoleMomentUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5073dc80_aec2_4a3b_8057_fababfcbfe11'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MagneticDipoleMomentUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MagneticDipoleMomentUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_5073dc80_aec2_4a3b_8057_fababfcbfe11',
    
    class_name='MagneticDipoleMomentUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5073dc80_aec2_4a3b_8057_fababfcbfe11',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MagneticDipoleMomentUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    