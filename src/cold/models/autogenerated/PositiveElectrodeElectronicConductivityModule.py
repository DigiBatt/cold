
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectronicConductivityModule import ElectronicConductivity







class PositiveElectrodeElectronicConductivity(ElectronicConductivity):
    """
    Class representing the `PositiveElectrodeElectronicConductivity` entity, which inherits from:
    - ElectronicConductivity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_43f77743_1af6_4a0f_9cc6_285c2a450549'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PositiveElectrodeElectronicConductivity'`
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
    obj = PositiveElectrodeElectronicConductivity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_43f77743_1af6_4a0f_9cc6_285c2a450549',
    
    class_name='PositiveElectrodeElectronicConductivity',
    
    cidemodKey="example_value",
    
    bpxKey="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_43f77743_1af6_4a0f_9cc6_285c2a450549',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PositiveElectrodeElectronicConductivity',
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
    

    
    

    

    