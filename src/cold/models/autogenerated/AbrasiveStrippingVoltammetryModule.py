
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VoltammetryModule import Voltammetry







class AbrasiveStrippingVoltammetry(Voltammetry):
    """
    Class representing the `AbrasiveStrippingVoltammetry` entity, which inherits from:
    - Voltammetry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#AbrasiveStrippingVoltammetry'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AbrasiveStrippingVoltammetry'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AbrasiveStrippingVoltammetry(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#AbrasiveStrippingVoltammetry',
    
    class_name='AbrasiveStrippingVoltammetry',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#AbrasiveStrippingVoltammetry',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AbrasiveStrippingVoltammetry',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    