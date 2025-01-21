
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ParticleRadiusModule import ParticleRadius







class NegativeElectrodeActiveMaterialParticleRadius(ParticleRadius):
    """
    Class representing the `NegativeElectrodeActiveMaterialParticleRadius` entity, which inherits from:
    - ParticleRadius

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bfe553c2_a63e_49b6_a209_0855dfc39724'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NegativeElectrodeActiveMaterialParticleRadius'`
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
    obj = NegativeElectrodeActiveMaterialParticleRadius(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bfe553c2_a63e_49b6_a209_0855dfc39724',
    
    class_name='NegativeElectrodeActiveMaterialParticleRadius',
    
    cidemodKey="example_value",
    
    bpxKey="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bfe553c2_a63e_49b6_a209_0855dfc39724',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NegativeElectrodeActiveMaterialParticleRadius',
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
    

    
    

    

    