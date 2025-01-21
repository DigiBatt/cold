
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricPotentialSignalModule import ElectricPotentialSignal







class ConstantPotentialSignal(ElectricPotentialSignal):
    """
    Class representing the `ConstantPotentialSignal` entity, which inherits from:
    - ElectricPotentialSignal

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0d3e8340_4229_4fd3_b6dd_763bd566551d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConstantPotentialSignal'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ConstantPotentialSignal(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0d3e8340_4229_4fd3_b6dd_763bd566551d',
    
    class_name='ConstantPotentialSignal',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0d3e8340_4229_4fd3_b6dd_763bd566551d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConstantPotentialSignal',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    