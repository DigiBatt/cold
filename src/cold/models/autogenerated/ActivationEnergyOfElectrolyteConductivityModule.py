
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ActivationEnergyModule import ActivationEnergy







class ActivationEnergyOfElectrolyteConductivity(ActivationEnergy):
    """
    Class representing the `ActivationEnergyOfElectrolyteConductivity` entity, which inherits from:
    - ActivationEnergy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8c16cb12_41c1_43bd_9e7c_2eea7b06a1f0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ActivationEnergyOfElectrolyteConductivity'`
        - **Alias**: `class_name`
    
    - `cidemodKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `cidemodKey`
    
    - `bpxKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `bpxKey`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ActivationEnergyOfElectrolyteConductivity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8c16cb12_41c1_43bd_9e7c_2eea7b06a1f0',
    
    class_name='ActivationEnergyOfElectrolyteConductivity',
    
    cidemodKey="example_value",
    
    bpxKey="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8c16cb12_41c1_43bd_9e7c_2eea7b06a1f0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ActivationEnergyOfElectrolyteConductivity',
        alias="class_name"
    )
    
    cidemodKey: Optional[str] = Field(
        None,
        alias="cidemodKey"
    )
    
    bpxKey: Optional[str] = Field(
        None,
        alias="bpxKey"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    