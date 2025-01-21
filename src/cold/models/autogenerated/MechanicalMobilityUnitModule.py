
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class MechanicalMobilityUnit(SIDimensionalUnit):
    """
    Class representing the `MechanicalMobilityUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_52ba3876_b51e_4670_a6f2_ce726abc2d3d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MechanicalMobilityUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MechanicalMobilityUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_52ba3876_b51e_4670_a6f2_ce726abc2d3d',
    
    class_name='MechanicalMobilityUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_52ba3876_b51e_4670_a6f2_ce726abc2d3d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MechanicalMobilityUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    