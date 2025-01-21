
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class AbsorbedDoseRateUnit(SIDimensionalUnit):
    """
    Class representing the `AbsorbedDoseRateUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_835f4e4e_680d_404c_8c73_92a6a570f6eb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AbsorbedDoseRateUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AbsorbedDoseRateUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_835f4e4e_680d_404c_8c73_92a6a570f6eb',
    
    class_name='AbsorbedDoseRateUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_835f4e4e_680d_404c_8c73_92a6a570f6eb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AbsorbedDoseRateUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    