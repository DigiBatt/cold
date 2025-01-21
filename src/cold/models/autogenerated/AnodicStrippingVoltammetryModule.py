
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StrippingVoltammetryModule import StrippingVoltammetry







class AnodicStrippingVoltammetry(StrippingVoltammetry):
    """
    Class representing the `AnodicStrippingVoltammetry` entity, which inherits from:
    - StrippingVoltammetry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#AnodicStrippingVoltammetry'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AnodicStrippingVoltammetry'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AnodicStrippingVoltammetry(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#AnodicStrippingVoltammetry',
    
    class_name='AnodicStrippingVoltammetry',
    
    iupacReference="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#AnodicStrippingVoltammetry',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AnodicStrippingVoltammetry',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    