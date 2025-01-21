
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharacterisationProcedureModule import CharacterisationProcedure







class MeasurementSystemAdjustment(CharacterisationProcedure):
    """
    Class representing the `MeasurementSystemAdjustment` entity, which inherits from:
    - CharacterisationProcedure

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#MeasurementSystemAdjustment'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MeasurementSystemAdjustment'`
        - **Alias**: `class_name`
    
    - `hasOutput` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasOutput`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `VIMTerm` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `VIMTerm`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MeasurementSystemAdjustment(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#MeasurementSystemAdjustment',
    
    class_name='MeasurementSystemAdjustment',
    
    hasOutput="example_value",
    
    definition="example_value",
    
    elucidation="example_value",
    
    VIMTerm="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#MeasurementSystemAdjustment',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MeasurementSystemAdjustment',
        alias="class_name"
    )
    
    hasOutput: Optional[str] = Field(
        None,
        alias="hasOutput"
    )
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    VIMTerm: Optional[str] = Field(
        None,
        alias="VIMTerm"
    )
    

    
    

    

    