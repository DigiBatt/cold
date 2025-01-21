
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VoltammetryModule import Voltammetry







class NormalPulseVoltammetry(Voltammetry):
    """
    Class representing the `NormalPulseVoltammetry` entity, which inherits from:
    - Voltammetry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#NormalPulseVoltammetry'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NormalPulseVoltammetry'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NormalPulseVoltammetry(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#NormalPulseVoltammetry',
    
    class_name='NormalPulseVoltammetry',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#NormalPulseVoltammetry',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NormalPulseVoltammetry',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    