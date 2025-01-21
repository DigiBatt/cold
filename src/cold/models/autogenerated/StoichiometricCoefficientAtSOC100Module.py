
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StoichiometricCoefficientModule import StoichiometricCoefficient







class StoichiometricCoefficientAtSOC100(StoichiometricCoefficient):
    """
    Class representing the `StoichiometricCoefficientAtSOC100` entity, which inherits from:
    - StoichiometricCoefficient

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_38ab058e_3912_48c2_a7eb_76d25d000820'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StoichiometricCoefficientAtSOC100'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StoichiometricCoefficientAtSOC100(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_38ab058e_3912_48c2_a7eb_76d25d000820',
    
    class_name='StoichiometricCoefficientAtSOC100',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_38ab058e_3912_48c2_a7eb_76d25d000820',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StoichiometricCoefficientAtSOC100',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    