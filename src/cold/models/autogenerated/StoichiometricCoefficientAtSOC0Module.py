
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StoichiometricCoefficientModule import StoichiometricCoefficient







class StoichiometricCoefficientAtSOC0(StoichiometricCoefficient):
    """
    Class representing the `StoichiometricCoefficientAtSOC0` entity, which inherits from:
    - StoichiometricCoefficient

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f22bd1ec_faca_4335_92a5_a1687154c622'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StoichiometricCoefficientAtSOC0'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StoichiometricCoefficientAtSOC0(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f22bd1ec_faca_4335_92a5_a1687154c622',
    
    class_name='StoichiometricCoefficientAtSOC0',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f22bd1ec_faca_4335_92a5_a1687154c622',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StoichiometricCoefficientAtSOC0',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    