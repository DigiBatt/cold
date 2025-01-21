
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class SquareCurrentQuarticTimePerMassUnit(SIDimensionalUnit):
    """
    Class representing the `SquareCurrentQuarticTimePerMassUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_cd9ad446_04f7_44ff_b9ea_ae7389574fa6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SquareCurrentQuarticTimePerMassUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SquareCurrentQuarticTimePerMassUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_cd9ad446_04f7_44ff_b9ea_ae7389574fa6',
    
    class_name='SquareCurrentQuarticTimePerMassUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_cd9ad446_04f7_44ff_b9ea_ae7389574fa6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SquareCurrentQuarticTimePerMassUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    