
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoatingModule import Coating



from .ActiveElectrodeModule import ActiveElectrode



from .ElectrodeModule import Electrode





from .BinderModule import Binder



from .ActiveMaterialModule import ActiveMaterial





class ElectrodeCoating(Coating, ActiveElectrode, Electrode):
    """
    Class representing the `ElectrodeCoating` entity, which inherits from:
    - Coating, ActiveElectrode, Electrode

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_403c300e_09b9_400b_943b_04e82a3cfb56'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrodeCoating'`
        - **Alias**: `class_name`
    
    - `hasBinder` (`Optional[Binder]`): 
        - **Default Value**: `None`
        - **Alias**: `hasBinder`
    
    - `hasAdditive` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasAdditive`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasActiveMaterial` (`Optional[ActiveMaterial]`): 
        - **Default Value**: `None`
        - **Alias**: `hasActiveMaterial`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrodeCoating(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_403c300e_09b9_400b_943b_04e82a3cfb56',
    
    class_name='ElectrodeCoating',
    
    hasBinder="example_value",
    
    hasAdditive="example_value",
    
    elucidation="example_value",
    
    hasActiveMaterial="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_403c300e_09b9_400b_943b_04e82a3cfb56',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrodeCoating',
        alias="class_name"
    )
    
    hasBinder: Optional[Binder] = Field(
        None,
        alias="hasBinder"
    )
    
    hasAdditive: Optional[str] = Field(
        None,
        alias="hasAdditive"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    hasActiveMaterial: Optional[ActiveMaterial] = Field(
        None,
        alias="hasActiveMaterial"
    )
    

    
    @validator("hasBinder", pre=True, always=True)
    def validate_hasBinder(cls, value):
        if value is not None and not isinstance(value, Binder):
            raise ValueError(f"Field 'hasBinder' must be an instance of 'Binder' or its subclass.")
        return value
    
    @validator("hasActiveMaterial", pre=True, always=True)
    def validate_hasActiveMaterial(cls, value):
        if value is not None and not isinstance(value, ActiveMaterial):
            raise ValueError(f"Field 'hasActiveMaterial' must be an instance of 'ActiveMaterial' or its subclass.")
        return value
    
    

    

    